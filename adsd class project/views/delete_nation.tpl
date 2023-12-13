<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delete National Player</title>
</head>
<body>
    <h1>Delete National Player</h1>
    <p>Are you sure you want to delete the national team player '{{player[2]}}' with ID '{{player[0]}}'?</p>
    <form action="/national/delete/{{player[0]}}" method="post">
        <input type="submit" value="Yes, Delete Player">
    </form>
    <a href="/">No, Cancel</a>
</body>
</html>
