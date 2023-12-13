<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit National Player</title>
</head>
<body>
    <h1>Edit National Player</h1>
    <form action="/national/edit/{{player[0]}}" method="post">
        <label for="jersey_number">Jersey Number:</label>
        <input type="text" name="jersey_number" value="{{player[1]}}" required><br>

        <label for="player_name">Player Name:</label>
        <input type="text" name="player_name" value="{{player[2]}}" required><br>

        <label for="team_name">Team Name:</label>
        <input type="text" name="team_name" value="{{player[3]}}" required><br>

        <input type="submit" value="Update Player">
    </form>

    <a href="/">Back to Home</a>
</body>
</html>
