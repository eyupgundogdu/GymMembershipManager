class Member:
    def __init__(self,name,membership_type,days_left):
        self.name = name
        self.membership_type = membership_type
        self.days_left = int(days_left)

    def __str__(self):
        return f'Name: {self.name} | Membership Type: {self.membership_type} | {self.days_left} days left!'

class Gym:
    def __init__(self):
        self.members = []

    def add_member(self):
        name = input('Name: ')
        m_type = input('Membership Type: ')
        days = int(input('How many days: '))
        new_member = Member(name,m_type,days)
        self.members.append(new_member)

    def list_members(self):
        for m in self.members:
            print(m)

    def workout_day(self):
        for m in self.members:
            if m.days_left > 0:
                m.days_left -= 1
                if m.days_left == 0:
                    print(f'Membership expired for [{m.name}]')
            else:
                print(f'{m.name} has no days left.')

    def renew_membership(self):
        name_in = input('Enter a name to renewe: ').strip().lower()
        found = False
        for m in self.members:
            if m.name.lower() == name_in:
                found = True
                extra = int(input(f'How many days to add for {m.name}: '))
                m.days_left += extra
                print(f'{m.name} now has {m.days_left} days.')
                break
        if not found:
            print('Member not found')

    def filter_gold_members(self):
        found = False
        for m in self.members:
            if m.membership_type.lower() == 'gold':
                print(m)
                found = True
        if not found:
            print('No Gold members found!')

def main():
    my_gym = Gym()

    while True:
        choice = input('1 - Add\n2 - List\n3 - Workout\n4 - Renew\n5 - Filter Gold\n6 - Exit\nchoice: ')
        if choice == '1':
            my_gym.add_member()
        elif choice == '2':
            my_gym.list_members()
        elif choice == '3':
            my_gym.workout_day()
        elif choice == '4':
            my_gym.renew_membership()
        elif choice == '5':
            my_gym.filter_gold_members()
        elif choice == '6':
            print('Exiting...')
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()
