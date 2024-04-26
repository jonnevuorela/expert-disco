<script>
    import Router from "svelte-spa-router";
    import Fingrid from "./Fingrid.svelte";
    import Ensto from "./Ensto.svelte";
    import Home from "./Home.svelte";

    const routes = {
        "/": Home,
        "/fingrid": Fingrid,
        "/ensto": Ensto,
    };
</script>

<nav>
    <a href="/#/fingrid">Fingrid</a>
    <a href="/#/ensto">Ensto</a>
</nav>
<Router {routes} />

<style>
    nav {
        display: flex;
        justify-content: center;
    }
    a {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 1.5rem;
        text-decoration: none;
        color: black;
        text-shadow: 1px 1px 7px sandybrown;
        box-shadow: 1px 1px 10px black;
        margin: 0 1rem;
        background-color: goldenrod;
        size: 1rem;
        height: 2rem;
        width: 5rem;
        margin-bottom: 1rem;
    }
</style>
