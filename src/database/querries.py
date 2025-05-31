class SQLiteQuerries:
    INSERT_TRANSACTION = '''
    INSERT INTO transactions (date, category_id, merchant_id, amount, payment_method_id, notes)
    VALUES (
        ?, 
        (SELECT id FROM categories WHERE name = ?), 
        (SELECT id FROM merchants WHERE name = ?), 
        ?, 
        (SELECT id FROM payment_methods WHERE name = ?), 
        ?
    );
    '''

    CREATE_CATEGORIES_TABLE = '''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    '''

    CREATE_MERCHANTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS merchants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    '''

    CREATE_PAYMENT_METHODS_TABLE = '''
    CREATE TABLE IF NOT EXISTS payment_methods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    '''

    CREATE_TRANSACTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        merchant_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        payment_method_id INTEGER NOT NULL,
        notes TEXT,

        FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL,
        FOREIGN KEY (merchant_id) REFERENCES merchants(id) ON DELETE SET NULL,
        FOREIGN KEY (payment_method_id) REFERENCES payment_methods(id) ON DELETE SET NULL
    );
    '''

    SELECT_ALL_TRANSACTIONS = 'SELECT * FROM transactions'
    DELETE_TRANSACTION = 'DELETE FROM transactions where id = ?;'

    INSERT_MERCHNAT = '''
    INSERT INTO merchants (name)
    SELECT ?
    WHERE NOT EXISTS (SELECT 1 FROM merchants WHERE name = ?);
    '''

    INSERT_PAYMENT_METHOD = '''
    INSERT INTO payment_methods (name)
    SELECT ?
    WHERE NOT EXISTS (SELECT 1 FROM payment_methods WHERE name = ?);
    '''

    INSERT_CATEGORIES = '''
    INSERT INTO categories (name)
    SELECT ?
    WHERE NOT EXISTS (SELECT 1 FROM categories WHERE name = ?);
    '''