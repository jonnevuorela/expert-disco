<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🏠</a>
    <h1 style="font:bold 2em tahoma;">Home</h1>
</div>
<div
    style="background-color: darkgrey; padding: 15em;
    display: flex; flex-direction: column; justify-content: center;"
>
    <p style="margin: 1em; font: 2em tahoma;">
        Welcome to the home page. Please use the navigation menu to use the
        apps.
    </p>
    <a id="navigator" href="/#/Counter">Counter</a>
    <a id="navigator" href="/#/Converter">Converter</a>
    <a id="navigator" href="/#/Weather">Weather</a>
    <a id="navigator" href="/#/Compensation">Compensation Calculator</a>
    <a id="navigator" href="/#/Participants">Participants</a>
</div>

<style>
    #navigator {
        display: flex;
        justify-content: center;
        grid: 1em;
        margin: 1ex;
        border: 5px groove blueviolet;
        border-radius: 5%;
        background-color: yellow;
        font: 2em sans-serif;
    }
    #navigator:hover {
        background-color: darkmagenta;
        color: cyan;
        text-decoration: underline;
        box-shadow: 5px 5px 5px 5px gold;
    }
</style>
