Bartosz Jnowiecki s25922

Dokumentacja Projektu: Password Manager
Opis projektu

Projekt Password Manager jest aplikacją konsolową do zarządzania hasłami. Umożliwia ona dodawanie, przeglądanie, edytowanie, usuwanie oraz wyszukiwanie haseł dla różnych witryn internetowych. Aplikacja zapewnia bezpieczne przechowywanie danych, wykorzystując szyfrowanie.
Wymagania

    Dodawanie nowej witryny:
        Użytkownik może dodać nową witrynę podając nazwę, link, login i hasło.
        Możliwość automatycznego generowania silnego hasła.

    Przeglądanie haseł:
        Użytkownik może przeglądać listę zapisanych witryn wraz z ich danymi.

    Generowanie silnych haseł:
        Aplikacja umożliwia generowanie silnych haseł o określonej długości.

    Usuwanie witryn:
        Użytkownik może usunąć wybraną witrynę z listy.

    Edycja danych witryny:
        Użytkownik może edytować dane już zapisanej witryny.

    Wyszukiwanie witryn po nazwie:
        Aplikacja umożliwia wyszukiwanie witryn na podstawie nazwy.

Funkcjonalność
Bezpieczeństwo

    Hasła są przechowywane w zaszyfrowanym pliku passwords.json za pomocą biblioteki cryptography.fernet.

Interfejs użytkownika

    Interaktywny interfejs konsolowy umożliwiający wybór operacji poprzez menu.

Autoryzacja

    Aplikacja wymaga podania poprawnych danych logowania (domyślnie admin/admin).

Implementacja
Struktura projektu

    Klasa Website:
        Reprezentuje dane witryny: nazwę, link, login oraz hasło.
        Metody to_dict i from_dict służą do konwersji obiektów na słownik i odwrotnie.

    Funkcje szyfrujące:
        encrypt_file(data, filename): szyfruje dane i zapisuje je do pliku.
        decrypt_file(filename): deszyfruje dane z pliku i zwraca je w postaci listy.

    Operacje na plikach:
        save_websites_to_file(websites, filename): zapisuje listę witryn do pliku.
        read_websites_from_file(filename): odczytuje listę witryn z pliku.

    Sprawdzanie siły hasła:
        check_password_strength(password): sprawdza, czy hasło spełnia wymagania bezpieczeństwa.

    Generowanie silnego hasła:
        generate_strong_password(length=12): generuje losowe, silne hasło o podanej długości.

    Wyszukiwanie witryn:
        search_website_by_name(websites, name): wyszukuje witrynę po nazwie i wyświetla jej dane.

Instrukcja Obsługi
    
    Uruchomienie programu:
        Aby uruchomić program, należy wywołać skrypt PswMenager.py w środowisku Python.

    Logowanie:
        Po uruchomieniu programu, użytkownik zostanie poproszony o podanie nazwy użytkownika i hasła. Domyślne dane logowania to admin/admin.

    Menu główne:
        Po zalogowaniu użytkownik zobaczy menu główne z opcjami:
            Dodaj witrynę
            Przeglądaj hasła
            Generuj silne hasło
            Usuń witrynę
            Edytuj witrynę
            Wyszukaj witrynę po nazwie
            Zakończ

    Dodawanie witryny:
        Wybierz opcję 1 i podaj nazwę, link, login oraz hasło do witryny. Możesz również wygenerować silne hasło automatycznie.

    Przeglądanie haseł:
        Wybierz opcję 2, aby zobaczyć listę zapisanych witryn wraz z ich danymi.

    Generowanie silnego hasła:
        Wybierz opcję 3, aby wygenerować silne hasło.

    Usuwanie witryny:
        Wybierz opcję 4 i podaj nazwę witryny, którą chcesz usunąć.

    Edycja witryny:
        Wybierz opcję 5, aby edytować dane zapisanej witryny. Możesz zmienić nazwę, link, login oraz hasło.

    Wyszukiwanie witryny po nazwie:
        Wybierz opcję 6 i podaj nazwę witryny, której szukasz.

    Zakończenie pracy:
        Wybierz opcję 7, aby zakończyć pracę programu i zapisać wszystkie zmiany.
