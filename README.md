# Onlayn Kutubxona Tizimi

Python dasturlash tilida yozilgan oddiy kutubxona boshqaruv tizimi.

## Klasslar

### `Book`
- **Maxfiy atributlar:** `__title`, `__author`, `__available`
- `borrow()` — kitobni olish (agar mavjud bo'lsa)
- `return_book()` — kitobni qaytarish
- `is_available()` — mavjudlik holatini olish

### `Library`
- Barcha kitoblarni saqlaydi
- `add_book(book)` — kitob qo'shish
- `get_book(title)` — kitobni topish
- `list_available_books()` — mavjud kitoblar ro'yxati

### `User`
- Foydalanuvchi faqat `Library` orqali kitob oladi/qaytaradi
- Kitobning `__available` atributiga bevosita kira olmaydi

## Foydalanish

```python
# Kitob yaratish
book1 = Book("1984", "Jorj Oruell")
book2 = Book("O'tgan Kunlar", "Abdulla Qodiriy")

# Kutubxona yaratish
library = Library()
library.add_book(book1)
library.add_book(book2)

# Foydalanuvchi yaratish
user = User("Ali")

# Kitob olish
user.borrow_book(library, "1984")        # Ali kitobni oldi
user.borrow_book(library, "1984")        # Mavjud emas

# Mavjud kitoblar
for b in library.list_available_books():
    print(b.get_title())  # O'tgan Kunlar

# Kitob qaytarish
user.return_book(library, "1984")        # Ali kitobni qaytardi
