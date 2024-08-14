class ExpenseManager:
    def __init__(self):
        self.participants=[]
        self.paid_status=[]
    def collect_participants(self):
        try:
            number=int(input("How many roomates do you have?"))
            if number<=0:
                raise ValueError("the amount should be greater than 0")
            for i in range(number):
                participant=input(f"enter the names of the roomates{i+1} name:").strip()
                self.participants.append(participant)
        except ValueError as e:
            print(f"invalid input: {e}")
    def calculate_and_display_shares(self,total_amount):
        if not self.participants:
            print("No roomates to split the bill")
            return 
        share_per_person=round(total_amount/len(self.participants),2)
        name_length=max(len(name) for name in self.participants)
        print("/n==bill split==")
        print(f"{'roomate':<{name_length}} {'share':>10}")
        print("-"*(name_length+12))
        for participant in self.participants:
            print(f"{participant:<{name_length}} Rs.{ share_per_person:>10.2f}")
    def record_payment_info(self):
        while True:
            payer=input("enter the name of the person").strip()
            if payer.lower()=='done':
                break
            if payer in self.participants:
                if payer not in self.paid_status:
                    self.paid_status.append(payer)
            else:
                print("not found")
    def display_payment_status(self):
        name_length=max(len(name)for name in self.participants)
        print("Payment status")
        print(f"{'roomate':<{name_length}}{'payment status':>15}")
        print("-"*(name_length+18))
        for participant in self.participants:
            status="paid" if participant in self.paid_status else "not paid"
            print("{participant:<{name_length}}{status:>15}")

def main():
    app=ExpenseManager()
    print("welcome")   
    app.collect_participants()
    try:
        total_bill=float(input("enter the bill amount"))
        if total_bill<=0:
            raise ValueError("the amount should be greater than 0")
    except ValueError as e:
        print("Invalid input:{e}")
        return
    app.calculate_and_display_shares(total_bill)
    app.record_payment_info()
    app.display_payment_status()
if __name__=="__main__":
    main()