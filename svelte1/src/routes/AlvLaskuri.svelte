<script>
    let hinta
    $: alv= 0.24*hinta
    $: if(hinta<0){
    alert ("hinta ei voi olla negatiivinen!")
}
</script>

<h1 style="font-family: Arial, Helvetica, sans-serif;">ALV Laskuri</h1>
<label for="alv">Anna hinta, lasken ALV:n</label>
    <input bind:value={hinta}>
{#if alv && alv>0}
<p>ALV on {alv}</p>
{:else} <p>Lasketaan alv..</p>
{/if}
