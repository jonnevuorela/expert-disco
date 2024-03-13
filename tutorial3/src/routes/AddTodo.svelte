<script>
    let m_title, m_completed;
    function save() {
        fetch(`https://jsonplaceholder.typicode.com/todos`, {
            method: "POST",
            body: JSON.stringify({
                title: m_title,
                completed: m_completed,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                (m_title = ""), (m_completed = false);
                alert(`Todo \"${json.title}\" saved`);
            });
    }
</script>

<h1>Add</h1>
<form>
    <div>
        <span>Title</span>
        <input bind:value={m_title} />
    </div>
    <div>
        <span>Completed</span>
        <input id="completed" type="checkbox" bind:checked={m_completed} />
    </div>
    <button on:click={save}>Save</button>
</form>

<style>
    span {
        display: inline-block;
        width: 80px;
        font-weight: bold;
    }
    div {
        margin: 8px;
    }
</style>
