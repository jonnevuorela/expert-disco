<script>
    let m_title, m_body, m_userId;
    function save() {
        fetch(`https://jsonplaceholder.typicode.com/posts`, {
            method: "POST",
            body: JSON.stringify({
                title: m_title,
                body: m_body,
                userId: m_userId,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                (m_title = ""), (m_body = ""), (m_userId = "");
                alert(`Post \"${json.title}\" saved`);
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
        <span>Body</span>
        <input bind:value={m_body} />
    </div>
    <div>
        <span>UserId</span>
        <input bind:value={m_userId} />
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
