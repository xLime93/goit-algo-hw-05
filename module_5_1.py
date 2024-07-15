def caching_fibonacci(n):
    """
    Створюємо порожній словник
    
    """
    cache = {}

    def fibonacci(n):
        if n <= 0: return 0
        elif n == 1: return 1
        else:
            """
            Спробуємо отримати значення зі словника
            
            """
            try:
                return cache[n]
            except:
                """
                Якщо значення не знайдено - додаємо
                
                """
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]
    
    return fibonacci(n)

"""
Перевіряємо працездатність функції
І що код працює правильно і не виконується два роки

"""
for i in range(701):
    print(i, caching_fibonacci(i))

