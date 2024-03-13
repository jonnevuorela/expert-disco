<script>
    import Todos from "./Todos.svelte";
    import AddTodo from "./AddTodo.svelte";
    import EditTodo from "./EditTodo.svelte";
    import Router, { push } from "svelte-spa-router";
    const routes = {
        "/": Todos,
        "/todos": Todos,
        "/edit": EditTodo,
        "/add": AddTodo,
    };
</script>

<nav>
    <a href="/#/todos">all todos</a>
    <a href="/#/add">add todo</a>
    <a href="/#/edit">edit todo</a>
</nav>
<Router {routes} />

<style>
    a {
        padding: 10px;
        background-color: lightgray;
        text-decoration: none;
    }
</style>
