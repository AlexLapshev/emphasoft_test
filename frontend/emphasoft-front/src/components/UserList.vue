<template>
    <div class="user-list">
        <ul>
            <li
                    v-for="user in users"
                    :key="user.id"
            >
                {{fullName(user)}}
            </li>
        </ul>
    </div>
</template>

<script>
  export default {
    name: "UserList",
    props: {
      users: {}
    },
    mounted() {
    },
    methods: {
      fullName: (user) => {
        return user.last_name + ' ' + user.first_name + ' ' + user.patronymic
      }
    }
  }
</script>

<style scoped lang="scss">
    ul {
        list-style: none;
    }
</style>