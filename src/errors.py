class StackEmptyError(IndexError): # исключение при попытке операции с пустым стеком
    pass


class QueueEmptyError(IndexError): # исключение при попытке операции с пустой очередью
    pass


class FlagError(ValueError): # исключение при передаче некорректного флага
    pass


class InvalidInputError(ValueError): # исключение при некорректном вводе данных
    pass