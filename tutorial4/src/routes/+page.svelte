<script>
    import Employees from "./Employees.svelte";
    import Edit from "./Edit.svelte";
    import Router, { push } from "svelte-spa-router";

    const routes = {
        "/": Employees,
        "/employees": Employees,
        "/edit": Edit,
    };
</script>

<nav>
    <a href="/#/employees">Employees</a>
    <a href="/#/edit">Edit</a>
</nav>
<Router {routes} />

<style>
    nav {
        display: flex;
        gap: 1rem;
    }

    a {
        text-decoration: none;
        background-color: navajowhite;
        padding: 1em;
        border-radius: 0.2em;
        box-shadow: 5px 5px 15px black;
    }
</style>
