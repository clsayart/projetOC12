from rest_framework.permissions import BasePermission, SAFE_METHODS

from epic_events.models import Customer, Event, Contract


class CustomerPermissions(BasePermission):

    def has_permission(self, request, view):
        print("request", request)
        print("request user", request.user)
        print("request methode", request.method)
        if request.user.role == "Support":
            print("role = support", request.method)
            return request.method in SAFE_METHODS
        return True

    def has_object_permission(self, request, view, obj):
        print("obj", obj)
        event = Event.objects.filter(support_contact=request.user, customer=obj)
        print(event)
        if request.user.role == "Support":
            if event:
                return request.method in SAFE_METHODS
            return False
        elif request.user.role == "Sales":
            print("object consumer sales user")
            if obj.sales_contact.id == request.user.id:
                print("je suis dans le if, je suis sales contact")
                return True
            return False
        elif request.user.role == "Management":
            return True


class ContractPermissions(BasePermission):

    def has_permission(self, request, view):
        # si c'est bien le client du commercial il peut créer un contrat
        if request.method == 'POST':
            customer = Customer.objects.get(id=int(request.data['customer']))
            if customer.sales_contact != request.user:
                return False
        # lecture seule pour le support
        if request.user.role == "Support":
            return request.method in SAFE_METHODS
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.sales_contact.id:
            return True
        # accès global pour les managers
        elif request.user.role == "Management":
            return True
        return False


class EventPermissions(BasePermission):

    def has_permission(self, request, view):
        print("event permission")
        if request.method == 'POST':
            print("1st if")
            contract = Contract.objects.get(id=int(request.data['contract']))
            print("contract post has permission", contract)
            print("contract.id", contract.id)
            customer = Customer.objects.get(id=contract.id)
            print("cus", customer)
            if request.user.role == "Support":
                print("request.user.role == Support")
                return request.method in SAFE_METHODS
            if customer.sales_contact != request.user:
                print("customer.sales_contact != request.user", customer.sales_contact, request.user)
                return False
        return True

    def has_object_permission(self, request, view, obj):
        print("event obj permission")
        print(request.data)
        contract = Contract.objects.get(id=str(obj.contract.id))
        print("contrat obj", contract)
        print(request.user.id, obj.support_contact.id, contract.sales_contact.id)
        if request.user.id == obj.support_contact.id or request.user.id == contract.sales_contact.id:
            print("request.user.id == obj.support_contact.id or request.user.id == contract.sales_contact.id:")
            return True
        elif request.user.role == "Management":
            print("management")
            return True
        print("false")
        return False
