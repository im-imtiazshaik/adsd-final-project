<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Football Players</title>
</head>
<body>
    <h1>National Team Players</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Jersey Number</th>
            <th>Player Name</th>
            <th>Team Name</th>
            <th>Action</th>
        </tr>
        % for player in national_players:
            <tr>
                <td>{{player[0]}}</td>
                <td>{{player[1]}}</td>
                <td>{{player[2]}}</td>
                <td>{{player[3]}}</td>
                <td>
                    <a href="/national/edit/{{player[0]}}">Edit</a>
                    <a href="/national/delete/{{player[0]}}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <h1>Club Team Players</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Jersey Number</th>
            <th>Player Name</th>
            <th>Club Name</th>
            <th>Action</th>
        </tr>
        % for player in club_players:
            <tr>
                <td>{{player[0]}}</td>
                <td>{{player[1]}}</td>
                <td>{{player[2]}}</td>
                <td>{{player[3]}}</td>
                <td>
                    <a href="/club/edit/{{player[0]}}">Edit</a>
                    <a href="/club/delete/{{player[0]}}">Delete</a>
                </td>
            </tr>
        % end
    </table>

    <a href="/national/add">Add National Player</a>
    <a href="/club/add">Add Club Player</a>
</body>
</html>
