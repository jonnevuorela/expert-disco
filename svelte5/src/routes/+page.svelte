<script>
    import Router from "svelte-spa-router";
    import Home from "./Home.svelte";
    import Tehtävä1 from "./1.svelte";
    import Tehtävä2 from "./2.svelte";

    const routes = {
        "/": Home,
        "/1": Tehtävä1,
        "/2": Tehtävä2,
    };
</script>

<nav>
    <a href="/#/">Home</a>
    <a href="/#/1">Tehtävä</a>
    <a href="/#/2">Tehtävä2</a>
</nav>

<Router {routes} />

<style>
    nav {
        background-color: cadetblue;
        border-bottom: 1px solid black;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 20px;
    }

    a {
        font-family: "Trebuchet MS", "Lucida Sans Unicode", "Lucida Grande",
            "Lucida Sans", Arial, sans-serif;
        color: seashell;
        border: 1px solid black;
        padding: 9px;
        text-shadow: 0 2px 0 rgba(0, 0, 0, 0.3);
        text-decoration: none;
        margin-right: 10px;
    }
</style>
