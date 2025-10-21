def singleton(cls):
    """
    Decorador Singleton.
    Asegura que solo exista una instancia de la clase decorada.
    """
    instancias = {}

    def get_instance(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]

    return get_instance
