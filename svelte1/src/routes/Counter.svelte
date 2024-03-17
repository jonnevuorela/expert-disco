<script>
    let visitors = 0;
</script>

<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🔙</a>
    <h1 style="font:bold 2em tahoma;">Counter</h1>
</div>
<div
    style="background-color: darkgrey; padding: 15em;
    display: flex; flex-direction: column; justify-content: center;;"
>
    <p style="font: 2em tahoma; display: flex; justify-content: center;">
        Visitors: {visitors}
    </p>
    <div style="display: flex; justify-content: center; padding: 1em;">
        <button
            on:click={() => {
                if (visitors > 0) {
                    visitors -= 1;
                } else {
                    alert("Visitors can't be negative");
                    reset();
                }
            }}>Decrement</button
        >
        <button
            on:click={() => {
                if (visitors < 10) {
                    visitors += 1;
                } else {
                    alert("Too many visitors!");
                }
            }}>Increment</button
        >
        <button
            on:click={() => {
                visitors = 0;
            }}>Reset</button
        >
    </div>
</div>
