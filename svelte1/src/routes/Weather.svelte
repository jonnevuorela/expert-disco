<script>
    let temp;
    let weather;
</script>

<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🔙</a>
    <h1 style="font:bold 2em tahoma;">Weather</h1>
</div>

<div
    style="background-color: darkgrey; padding: 15em;
    display: flex; flex-direction: column; justify-content: center;"
>
    <p style="margin: 1em; font: 2em tahoma;">Please enter the temperature.</p>
    <input
        style="margin: 1em; width: 10em;"
        type="text"
        bind:value={temp}
        placeholder="temperature C°"
    />
    <button
        style="margin: 1em; height: 2em;width: 10em;"
        on:click={() => {
            let tempNum = Number(temp);
            if (tempNum < -40) {
                weather = "freezing";
            } else if (tempNum >= -40 && tempNum <= -20) {
                weather = "crisp";
            } else if (tempNum >= -19 && tempNum <= -5) {
                weather = "chilly";
            } else if (tempNum >= -4 && tempNum <= 5) {
                weather = "cool";
            } else if (tempNum >= 6 && tempNum <= 15) {
                weather = "warm";
            } else if (tempNum >= 16 && tempNum <= 25) {
                weather = "very warm";
            } else if (tempNum >= 26 && tempNum <= 40) {
                weather = "It's hot";
            } else if (tempNum >= 40) {
                weather = "very hot";
            }
        }}
    >
        Weather Converter
    </button>
    {#if weather}
        <p style="margin: 1em; font: 2em tahoma;">
            The weather is {weather}
        </p>
    {/if}
</div>
