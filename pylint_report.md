Pylint report for the application is as follows:

```************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:16:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:28:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:51:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:51:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:83:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:94:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:83:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:103:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:108:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:109:4: W0621: Redefining name 'spot' from outer scope (line 108) (redefined-outer-name)
app.py:108:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:164:12: R0916: Too many boolean expressions in if statement (6/5) (too-many-boolean-expressions)
app.py:211:33: E0606: Possibly using variable 'spot_id' before assignment (possibly-used-before-assignment)
app.py:132:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:214:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:215:4: W0621: Redefining name 'spot' from outer scope (line 108) (redefined-outer-name)
app.py:237:12: R0916: Too many boolean expressions in if statement (6/5) (too-many-boolean-expressions)
app.py:214:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:284:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:306:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:316:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:364:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:365:4: W0621: Redefining name 'spot' from outer scope (line 108) (redefined-outer-name)
app.py:379:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:379:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:394:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:394:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:413:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:426:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:429:4: W0621: Redefining name 'user' from outer scope (line 426) (redefined-outer-name)
app.py:426:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:440:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module db
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:11:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:21:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:21:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module spots
spots.py:1:0: C0114: Missing module docstring (missing-module-docstring)
spots.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:31:0: R0913: Too many arguments (8/5) (too-many-arguments)
spots.py:31:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
spots.py:60:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:84:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:157:0: R0913: Too many arguments (8/5) (too-many-arguments)
spots.py:157:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
spots.py:169:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:173:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:191:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:200:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:213:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:217:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:231:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:251:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:258:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:266:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:270:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:274:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:278:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:302:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:316:0: C0116: Missing function or method docstring (missing-function-docstring)
spots.py:320:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:38:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:1:0: R0801: Similar lines in 2 files
==app:[201:207]
==spots:[50:56]
                     continent,
                     country,
                     title,
                     max_incline,
                     skill_level,
                     aspect, (duplicate-code)
users.py:1:0: R0801: Similar lines in 2 files
==app:[273:278]
==spots:[51:56]
                              country,
                              title,
                              max_incline,
                              skill_level,
                              aspect, (duplicate-code)

------------------------------------------------------------------
Your code has been rated at 8.11/10 (previous run: 8.11/10, +0.00)```


<h1>Report breakdown<h1>


```Missing module docstring (missing-module-docstring), Missing function or method docstring (missing-function-docstring)```
Docstrings have been left out intentionally


```app.py:51:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)```
In some cases, the function returns abort(403). This may happen if data is pushed in from outside the application and then the function performs exactly like it's supposed to without return statements. 


```Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)```

From the app:

```        if user_id:
            session["user_id"] = user_id
            return redirect("/home")
        else:
            flash("ERROR: Wrong username or password")
            return redirect("/")```

Here the else-statement is more explanatory than it would be to leave it out.


```Redefining name 'spot' from outer scope (line 108) (redefined-outer-name)```

This error comes from the fact that spot is the name of the function in @spot route and then it is used as variable inside that function. 
However, the function is called only once the route loads, so using the same name doesn't cause any problems and the variable name is easily understood.

```Dangerous default value [] as argument (dangerous-default-value)```
Doesn't cause danger or issues here. 


``Too many arguments (8/5) (too-many-arguments) / Too many positional arguments (8/5) (too-many-positional-arguments)````
The form where data is originating from is rather large and handing many variables this way is probably not ideal. However, it works fine, so this can be disregarded.

```users.py:1:0: R0801: Similar lines in 2 files
==app:[201:207]
==spots:[50:56]
                     continent,
                     country,
                     title,
                     max_incline,
                     skill_level,
                     aspect, (duplicate-code)
users.py:1:0: R0801: Similar lines in 2 files
==app:[273:278]
==spots:[51:56]
                              country,
                              title,
                              max_incline,
                              skill_level,
                              aspect, (duplicate-code)
```

These parts are similar and maybe could be hard-coded into some container, but, yet again, this works now fine.
