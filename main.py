def sieve_of_eratosthenes(n):
    # Создаем список логических значений, где True означает, что число является простым
    primes = [True] * (n + 1)
    p = 2  # Первый простой номер

    while (p * p <= n):
        # Если primes[p] не изменился, значит p — простое число
        if primes[p]:
            # Обновляем все кратные p, начиная с p*p
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    # Создаем список простых чисел
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Пример использования
if __name__ == "__main__":
    n = int(input("Введите натуральное число: "))
    prime_numbers = sieve_of_eratosthenes(n)
    print(f"Простые числа до {n}: {prime_numbers}")
