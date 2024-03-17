<script>
    let fahrenheit;
    let celsius;
</script>

<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🔙</a>
    <h1 style="font:bold 2em tahoma;">Converter</h1>
</div>
<div
    style="background-color: darkgrey; padding: 15em;
    display: flex; flex-direction: column; justify-content: center;"
>
    <p style="font:2em tahoma; margin: 1em;">
        Please input the temperature you are converting. (F°)
    </p>
    <input
        type="number"
        bind:value={fahrenheit}
        style="font-size: 20pt; margin: 1em;"
    />
    {#if celsius}
        <p style="font-size: 20pt; margin: 1em;">
            The temperature in Celsius is: {celsius}C°
        </p>
    {/if}
    <button
        on:click={() => {
            celsius = ((fahrenheit - 32) * 5) / 9;
            celsius = celsius.toFixed(2);
        }}
        style="font-size: 20pt; height: 2em; width: 5em; margin: 1em;"
    >
        Convert
    </button>
</div>
