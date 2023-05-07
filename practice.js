<!DOCTYPE html>
<html>
<head>
<title>Calculating your age in dog years</title>

    <script type="text/javascript">

    function cyears (form) {
    form.dogage.value = form.myage.value * 7
    }
    </script>

</head>

<body>

        <b>Find out your age in dog years</b>

        <form method="post">


            <table>

            <tr>

                <td>Enter you age:</td>
                <td><input type="text" name="myage" size=15></td>

            </tr>

            <tr>
                <td>
                <input type="button" value="Calculate" onclick="cyears(this.form)">
                </td>

            </tr>

            <tr>
                <td>Your age in dog Years is:</td>
                <td><input type="text" name="dogage" size="15"</td>

            </tr>
            </table>

        </form>
</body>
</html>