<script>
    let todos = [];
    fetch("https://jsonplaceholder.typicode.com/todos")
        .then((response) => response.json())
        .then((json) => (todos = json));
</script>

<h1>Todos</h1>
{#if todos.length}
    <table>
        {#each todos as todo}
            <tr>
                <td>{todo.id}</td>
                <td>{todo.userId}</td>
                <td>{todo.title}</td>
                <td>{todo.completed}</td>
            </tr>
        {/each}
    </table>
{/if}

<style>
    tr,
    td {
        border: 1px solid black;
    }
</style>
