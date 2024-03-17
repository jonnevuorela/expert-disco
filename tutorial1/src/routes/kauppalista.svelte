<script>
    let kokonaishinta=0, tuotteet=[], hinta, tuotenimi;

    function lisaaTuote(){
        console.log("Lisätään tuote")
        let tuote = {nimi: tuotenimi, hinta: hinta, readonly: true}
        tuotteet = [...tuotteet, tuote]
        tuotenimi = "",hinta=""
    }

    function modify(index) {
        tuotteet[index].readonly = false
    }   
    function save(index) {
        tuotteet[index].readonly = true
    }

    $: kokonaishinta =
    tuotteet.reduce((total, current) => {return total +
    current.hinta}, 0)
</script>

<h3>Lisää tuote kauppalistaan</h3>
<div><label for="tuotenimi">Tuotenimi</label></div>
<input id="tuotenimi"  bind:value={tuotenimi}>
<div><label for="hinta">Tuotteen hinta</label></div>
<input type=number id="hinta" bind:value={hinta}/>€<br/>
<button on:click={lisaaTuote}>Lisää tuote</button>
{#if tuotteet.length !=0}
<h3>Kauppalista</h3>
{/if}
<ul>
    {#each tuotteet as tuote, index}
    <li>
        <input id={tuote.nimi} value={tuote.nimi} readonly={tuote.readonly}/>
        <input type=number bind:value={tuote.hinta} readonly={tuote.readonly}/>€
        {#if tuote.readonly}
        <button on:click={()=>modify(index)}>Modify</button>
        {:else}
        <button on:click={()=>save(index)}>Save</button>
        {/if}
    </li>
    {/each}
</ul>

{#if kokonaishinta != 0}
<p>Yhteensä: {kokonaishinta}€</p>
{/if}
