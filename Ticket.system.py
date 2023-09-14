import re

class HelpDeskTicket:
    ticket_counter = 2000
    

    def __init__(self, user_name, employee_id, email, issue):
        HelpDeskTicket.ticket_counter += 1
        HelpDeskTicket.open_tickets += 1
        self.ticket_number = HelpDeskTicket.ticket_counter + 2000
        self.user_name = user_name
        self.employee_id = employee_id
        self.email = email
        self.issue = issue
        self.response = "Not Yet Provided"
        self.status = "Open"

    def provide_solution(self, response):
        self.response = response
        self.status = "Closed"
        HelpDeskTicket.open_tickets -= 1
        HelpDeskTicket.resolved_tickets += 1

    def reopen(self):
        self.response = "Not Yet Provided"
        self.status = "Reopened"
        HelpDeskTicket.open_tickets += 1
        HelpDeskTicket.resolved_tickets -= 1

    def resolve_password_reset(self):
        new_password = self.employee_id[:2] + self.user_name[:3]
        self.response = f"New password generated: {new_password}"
        self.status = "Closed"
        HelpDeskTicket.open_tickets -= 1
        HelpDeskTicket.resolved_tickets += 1

    def display(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"User Name: {self.user_name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Email: {self.email}")
        print(f"Issue: {self.issue}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}\n")

    @staticmethod
    def statistics():
        print("\nTicket Statistics\n")
        print(f"Total Tickets: {HelpDeskTicket.ticket_counter}")
        print(f"Resolved Tickets: {HelpDeskTicket.resolved_tickets}")
        print(f"Open Tickets: {HelpDeskTicket.open_tickets}\n")


def main():
    tickets = [
        HelpDeskTicket("PRIYANKA", "priyanka", "priyank@example.com", "Network connectivity issue"),
        HelpDeskTicket("ATUL", "atul", "atul@example.com", "Software installation problem"),
        HelpDeskTicket("Charlie", "CHL789", "charlie@example.com", "Password reset needed"),
        HelpDeskTicket("David", "DAV012", "david@example.com", "Printer not responding"),
        HelpDeskTicket("RITIKA", "ritika1", "ritu@example.com", "Email not sending")
    ]

    for ticket in tickets:
        ticket.display()

    tickets[2].resolve_password_reset()
    tickets[1].provide_solution("Software successfully installed.")

    for ticket in tickets:
        ticket.display()

    tickets[1].reopen()
    tickets[1].display()

    HelpDeskTicket.statistics()


if __name__ == "__main__":
    main()
