<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Club Player</title>
</head>
<body>
    <h1>Add Club Player</h1>
    <form action="/club/add" method="post">
        <label for="jersey_number">Jersey Number:</label>
        <input type="text" name="jersey_number" required><br>

        <label for="player_name">Player Name:</label>
        <input type="text" name="player_name" required><br>

        <label for="club_name">Club Name:</label>
        <input type="text" name="club_name" required><br>

        <input type="submit" value="Add Player">
    </form>

    <a href="/">Back to Home</a>
</body>
</html>
