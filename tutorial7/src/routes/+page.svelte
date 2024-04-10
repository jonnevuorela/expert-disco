<script>
    import Testi1 from "./Testi1.svelte";
    import Testi2 from "./Testi2.svelte";

    let q1 = false;
    let q2 = false;

    function testi1() {
        q1 = !q1;
        q2 = false;
    }
    function testi2() {
        q2 = !q2;
        q1 = false;
    }
</script>

<div id="header">
    <h1>Digitraffic testejä</h1>
    q1: {q1}
    q2: {q2}
    <button on:click={testi1}>Testi 1</button>
    <button on:click={testi2}>Testi 2</button>
</div>
<div id="table">
    {#if q1}
        <Testi1 />
    {/if}
    {#if q2}
        <Testi2 />
    {/if}
</div>
