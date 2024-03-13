<script>
    let todos = [];
    let selectedTodo;
    let editTodo;

    function showForm() {
        fetch(`https://jsonplaceholder.typicode.com/todos/${selectedTodo}`)
            .then((response) => response.json())
            .then((json) => (editTodo = json));
    }
    function save() {
        fetch(`https://jsonplaceholder.typicode.com/todos/${editTodo.id}`, {
            method: "PUT",
            body: JSON.stringify({
                id: editTodo.id,
                title: editTodo.title,
                completed: editTodo.completed,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                editTodo = null;
                alert(`Todo\"${json.title}\" saved`);
            });
    }
    fetch("https://jsonplaceholder.typicode.com/todos")
        .then((response) => response.json())
        .then((json) => (todos = json));
</script>

<p>Choose the editable Todo</p>
<select bind:value={selectedTodo} on:change={showForm}>
    <option>Choose todo </option>
    {#each todos as todo}
        <option value={todo.id}>{todo.title}</option>
    {/each}
</select>

{#if editTodo}
    <h2>Modify</h2>
    <form>
        <input type="hidden" value={editTodo.id} />
        <div>
            <span>Title</span>
            <input bind:value={editTodo.title} />
        </div>
        <div>
            <span>Completed</span>
            <input
                id="completed"
                type="checkbox"
                bind:checked={editTodo.completed}
            />
        </div>
        <button on:click={save}>Save</button>
    </form>
{/if}

<style>
    span {
        display: inline-block;
        width: 80px;
        font-weigth: bold;
    }
    div {
        margin: 8px;
    }
</style>
