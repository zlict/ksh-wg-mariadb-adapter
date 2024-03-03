# MariaDB Adapter for Python

Not for use in production

## Usage 

### Connect

```py
db = ksh_wg_mariadb_adapter.connect("lernumgebung_mariadb-server", "root", "mariadb", datenbank)

if db.test():
  print("Hurra! Die Verbindung zur Datenbank klappt :)")
else: 
  print("Uups! Da ging noch was schief :(")
```

### Select

List tables:

```py
tabellen = db.tables()
print(tabellen)
```

Select all data from a table:

```py
daten = db.select("noten")
print(daten)
```
Condition:

```py
daten = db.select("noten", where="note > 5")
```

Order:

```py
daten = db.select("noten", order_by="note ASC")
daten = db.select("noten", order_by="note ASC, name DESC")
```

### Insert

```py
new_tupel = { "name": "Hans Muster", "note": 5.5 }
db.insert("noten", new_tupel)
```

### Update 

```py
changes = { "name": "Hans Muster", "note": 4.5 }
db.update("noten", changes, where="id = 1")
```

### Delete

```py
db.delete("noten", where="id = 1")
```
