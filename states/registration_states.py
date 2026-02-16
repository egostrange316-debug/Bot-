class RegistrationStates:
    NEW = 'new'
    PENDING = 'pending'
    ACTIVE = 'active'
    SUSPENDED = 'suspended'
    DELETED = 'deleted'

    @staticmethod
    def choices():
        return [RegistrationStates.NEW, RegistrationStates.PENDING, RegistrationStates.ACTIVE, RegistrationStates.SUSPENDED, RegistrationStates.DELETED]