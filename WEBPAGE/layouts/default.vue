<template>
  <div class="flex flex-col">
    <Navbar/>
    <div class="min-h-screen w-full flex mx-auto justify-center max-w-lg md:max-w-3xl lg:max-w-5xl px-4 md:px-0">
      <slot></slot>
    </div>
    <Footer/>
  </div>
</template>