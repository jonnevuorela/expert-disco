<script>
    import Router from "svelte-spa-router";
    import Home from "./Home.svelte";
    import Add from "./Add.svelte";
    import Edit from "./Edit.svelte";
    import Posts from "./Posts.svelte";
    import Delete from "./Delete.svelte";

    const routes = {
        "/": Home,
        "/Add": Add,
        "/Edit": Edit,
        "/Posts": Posts,
        "/Delete": Delete,
    };
</script>

<div id="navi">
    <nav>
        <a href="/#">Home</a>
        <a href="/#/Add">Add</a>
        <a href="/#/Edit">Edit</a>
        <a href="/#/Posts">Posts</a>
        <a href="/#/Delete">Delete</a>
    </nav>
</div>
<Router {routes} />

<style>
    #navi {
        display: flex;
        flex-direction: flex-start;
        padding: 0.5em;
        background-color: magenta;
        border: 1px solid whitesmoke;
    }
    nav {
        display: flex;
        flex-direction: row;
        gap: 0.1em;
    }
    a {
        border-radius: 0.2em;
        border: 0.2em groove blueviolet;
        padding: 0.5em;
        text-decoration: none;
        color: black;
    }
    a:hover {
        box-shadow: yellowgreen 0.1em 0.1em 1em;
        background-color: blueviolet;
        color: white;
    }
</style>
