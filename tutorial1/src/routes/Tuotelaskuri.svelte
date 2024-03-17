<script>
    let hinnat=[]
    let hinta

    function lisaaHinta(){
        hinta = parseInt(hinta)
        hinnat =[...hinnat, hinta]
        hinta =""
    }
    
    $: sum = hinnat.reduce((total,current)=>total + current, 0)

    $:console.log(hinnat)


</script>

<p>Tuotteiden yhteenlaskettu summa on </p>
<p>{hinnat.join(" + ")} ={sum} </p>

<p>Lisättävän tuotteen hinta: <input bind:value={hinta}></p>
<button on:click={lisaaHinta}>
    lisää hinta
</button>