<script>
    let posts = [];
    fetch("https://jsonplaceholder.typicode.com/posts")
        .then((response) => response.json())
        .then((json) => (posts = json));
    $: console.log("posts", posts);
</script>

<h1>Posts</h1>
{#if posts.length}
    <table>
        <th>Id</th>
        <th>Title</th>
        <th>Body</th>
        <th>User Id</th>

        {#each posts as post}
            <tr>
                <td>{post.id}</td>
                <td>{post.title}</td>
                <td>{post.body}</td>
                <td>{post.userId}</td>
            </tr>
        {/each}
    </table>
{/if}

<style>
    th,
    tr,
    td {
        border: 1px solid black;
    }
</style>
