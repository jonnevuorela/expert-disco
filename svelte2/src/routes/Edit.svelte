<script>
    let posts = [];
    let selectedPost;
    let editPost;

    function showForm() {
        fetch(`https://jsonplaceholder.typicode.com/posts/${selectedPost}`)
            .then((response) => response.json())
            .then((json) => (editPost = json));
    }
    function save() {
        fetch(`https://jsonplaceholder.typicode.com/posts/${editPost.id}`, {
            method: "PUT",
            body: JSON.stringify({
                id: editPost.id,
                title: editPost.title,
                completed: editPost.completed,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                editPost = null;
                alert(`Post\"${json.title}\" saved`);
            });
    }
    fetch("https://jsonplaceholder.typicode.com/posts")
        .then((response) => response.json())
        .then((json) => (posts = json));
</script>

<p>Choose the editable Post</p>
<select bind:value={selectedPost} on:change={showForm}>
    <option>Choose post </option>
    {#each posts as post}
        <option value={post.id}>{post.title}</option>
    {/each}
</select>

{#if editPost}
    <h2>Modify</h2>
    <form>
        <input type="hidden" value={editPost.id} />
        <div>
            <span>Title</span>
            <input bind:value={editPost.title} />
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
