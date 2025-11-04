"""
Cloud Service Management Tracker
--------------------------------
This mini project simulates tracking and managing cloud resources 
like virtual machines, storage, and databases in a cloud environment.

Features:
- Add, update, and remove cloud services
- Track service usage and cost
- Generate reports and visualize resource consumption
- Designed for educational and demonstration purposes

Author: Akshaya P
"""

import datetime
import random
from prettytable import PrettyTable

# -----------------------------
# Cloud Service Class
# -----------------------------
class CloudService:
    def __init__(self, service_id, service_name, service_type, cost_per_hour):
        self.service_id = service_id
        self.service_name = service_name
        self.service_type = service_type
        self.cost_per_hour = cost_per_hour
        self.usage_hours = 0
        self.status = "Active"
        self.creation_date = datetime.datetime.now()

    def add_usage(self, hours):
        if self.status == "Active":
            self.usage_hours += hours
        else:
            print(f"[WARNING] Cannot add usage. {self.service_name} is inactive.")

    def calculate_cost(self):
        return self.usage_hours * self.cost_per_hour

    def deactivate(self):
        self.status = "Inactive"

# -----------------------------
# Cloud Management System
# -----------------------------
class CloudServiceManager:
    def __init__(self):
        self.services = {}

    def add_service(self, service_name, service_type, cost_per_hour):
        service_id = len(self.services) + 1
        new_service = CloudService(service_id, service_name, service_type, cost_per_hour)
        self.services[service_id] = new_service
        print(f"[INFO] Added new service: {service_name} ({service_type})")

    def remove_service(self, service_id):
        if service_id in self.services:
            self.services[service_id].deactivate()
            print(f"[INFO] Deactivated service ID: {service_id}")
        else:
            print("[ERROR] Service ID not found.")

    def add_usage(self, service_id, hours):
        if service_id in self.services:
            self.services[service_id].add_usage(hours)
            print(f"[INFO] Added {hours} hours usage to service ID {service_id}")
        else:
            print("[ERROR] Service ID not found.")

    def show_all_services(self):
        table = PrettyTable(["ID", "Service Name", "Type", "Status", "Usage (hrs)", "Cost ($)", "Created"])
        for s in self.services.values():
            table.add_row([
                s.service_id,
                s.service_name,
                s.service_type,
                s.status,
                s.usage_hours,
                round(s.calculate_cost(), 2),
                s.creation_date.strftime("%Y-%m-%d")
            ])
        print(table)

    def total_cost(self):
        total = sum(s.calculate_cost() for s in self.services.values())
        print(f"\n💰 Total Cloud Cost: ${round(total, 2)}")

    def generate_report(self):
        print("\n📊 Cloud Service Usage Report")
        print("------------------------------")
        for s in self.services.values():
            print(f"- {s.service_name} ({s.service_type}) -> {s.usage_hours} hrs, ${s.calculate_cost()}")

# -----------------------------
# Simulation Function
# -----------------------------
def demo_simulation():
    print("=== ☁️ Cloud Service Management Tracker ===\n")

    manager = CloudServiceManager()
    manager.add_service("Compute Engine", "VM", 0.25)
    manager.add_service("Cloud Storage", "Storage", 0.10)
    manager.add_service("SQL Database", "Database", 0.30)

    # Simulate random usage
    for i in range(1, 4):
        usage = random.randint(10, 50)
        manager.add_usage(i, usage)

    manager.show_all_services()
    manager.total_cost()
    manager.generate_report()

    # Deactivate a service
    manager.remove_service(2)
    print("\nAfter deactivating Cloud Storage:")
    manager.show_all_services()
    manager.total_cost()

if __name__ == "__main__":
    demo_simulation()
