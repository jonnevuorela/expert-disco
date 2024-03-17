<script>
    let distance;
    let commuters;
    let compensation;
    let rate;
</script>

<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🔙</a>
    <h1 style="font:bold 2em tahoma;">Compensation calculator</h1>
</div>
<div
    style="background-color: darkgrey; padding: 15em;
    display: flex; flex-direction: column; justify-content: center;"
>
    <p style="margin: 1em; font: 3ex tahoma;">
        Please enter the travel distance and the number of commuters to
        calculate the compensation.
    </p>
    <input
        type="number"
        id="distance"
        name="distance"
        placeholder="Distance in km"
        style="margin: 1em; font: 1em tahoma; width: 12em; height: 1em;"
        bind:value={distance}
    />
    <input
        type="number"
        id="commuters"
        name="commuters"
        placeholder="Number of commuters"
        style="margin: 1em; font: 1em tahoma; width: 12em; height: 1em;"
        bind:value={commuters}
    />
    <button
        style="margin: 1em; font: 1em tahoma; width: 12em; height: 2em;"
        on:click={() => {
            rate = 0.49 + commuters * 0.04;
            compensation = (distance * rate).toFixed(2);
        }}
    >
        Calculate
    </button>
    {#if compensation}
        <p style="font: 1em tahoma; margin: 1em;">
            The travel compensation is {compensation}€.
        </p>
    {/if}
</div>
