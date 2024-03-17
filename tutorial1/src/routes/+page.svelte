
<script>
    import Hobbies from "./Hobbies.svelte";
    import AlvLaskuri from "./AlvLaskuri.svelte";
    import Tuotelaskuri from "./Tuotelaskuri.svelte";
    import Kauppalista from "./kauppalista.svelte";
    import Router, {push} from "svelte-spa-router";
    let name ="world";
    const routes ={
        "/": Hobbies,
        "/alv": AlvLaskuri,
        "/tuotelaskuri": Tuotelaskuri,
        "/kauppalista": Kauppalista
    }
</script>

<nav>
    <a href="/#/">Home</a>
    <a href="/#/alv">AlvLaskuri</a>
    <a href="/#/tuotelaskuri">Tuotelaskuri</a>
    <a href="/#/kauppalista">Kauppalista</a>
</nav>

<h1 style="font-family: monospace;">
    Hello {name.toUpperCase()}!
</h1>

<p>Tervetuloa yritykseni sivuille</p>

<Hobbies/>

<style>
    a {
        padding: 10px;
        background-color: aqua;
        border-radius: 5px;
        border-color: aquamarine;
        
    }
    p{
        color:red;
    }
</style>

<Router {routes}/>