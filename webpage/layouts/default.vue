<template>
  <div class="container mx-auto flex flex-col h-screen">
    <Navbar/>
    <div class="max-h-min flex-1">
      <slot></slot>
    </div>
    <Footer/>
  </div>
</template>