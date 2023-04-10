<template>
  <div>
    <div class="py-20 px6 bg-teal-700 text-center">
      <h1 class="mb-12 text-5xl text-white">Find a job anywhere</h1>

      <nuxt-link
        to="/browse"
        class="inline-block py-4 px-8 bg-teal-900 text-white rounded-xl"
        >Browse</nuxt-link
      >
    </div>

    <div class="py-10 px-6">
      <h2 class="mb-8 text-2xl text-center">Newest jobs</h2>

      <div class="space-y-4">
        <div class="p-6 flex items-center justify-between bg-gray-100">
          <div>
            <h1 class="text-xl font-semibold">The job position</h1>
            <p class="text-gray-600">The company name</p>
          </div>
          <div>
            <h1 class="font-semibold">Worldwide</h1>
            <p class="text-gray-600">$90-120$</p>
          </div>
          <div>
            <p>Posted Dec. 1. 2022</p>
          </div>
          <div>
            <nuxt-link
              to="/browse/1"
              class="py-4 px-6 bg-teal-700 text-white rounded-xl"
              >Detail</nuxt-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>