<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <?php
    include 'token.php';
    $clantag = "#92LUCRR9";
    $token = $tokenCode;
    $url = "https://api.clashofclans.com/v1/clans/" . urlencode($clantag) . "/currentwar";
    $ch = curl_init($url);
    $headr = array();
    $headr[] = "Accept: application/json";
    $headr[] = "Authorization: Bearer " . $token;
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headr);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $res = curl_exec($ch);
    $data = json_decode($res, true);
    curl_close($ch);
    if (isset($data["reason"])) {
        $errormsg = true;
    }
    $warMembers = $data["clan"]["members"];
    $opponentMembers = $data["opponent"]["members"];
    ?>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        <?php echo $data["clan"]["name"]; ?>
    </title>
    <style>
        <?php include 'style.css'; ?>
    </style>
</head>

<body>
    <h1>Our Members</h1>
    <table>
        <?php foreach ($warMembers as $members) { ?>
            <tr>
                <td>
                    <?php echo $members["name"] ?>
                </td>
                <td>
                    <span>Town Hall Level</span>
                    <?php echo $members["townhallLevel"] ?>
                </td>
                <td>
                    <span>Been Attacked Ct:</span>
                    <?php echo $members["opponentAttacks"] ?>
                </td>
            </tr>
            <?php
        }

        ?>

    </table>
    <h1>Enemies Members</h1>
    <table>
        <?php foreach ($opponentMembers as $members) { ?>
            <tr>
                <td>
                    <?php echo $members["name"] ?>
                </td>
                <td>
                    <span>Town Hall Level</span>
                    <?php echo $members["townhallLevel"] ?>
                </td>
            </tr>
            <?php
        }

        ?>

    </table>
</body>

</html>