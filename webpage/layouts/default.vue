<template>
  <div class="flex flex-col">
    <Navbar/>
    <div class="min-h-screen w-full flex mx-auto justify-center max-w-sm md:max-w-lg px-4 md:px-0">
      <slot></slot>
    </div>
    <Footer/>
  </div>
</template>