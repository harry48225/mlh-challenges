<script lang="ts">
  import Matter, { Bodies, Composite, Mouse, Runner, World } from 'matter-js';
  import { Render } from 'matter-js';
  import { Engine } from 'matter-js';
  import { onMount } from 'svelte';
  
  const engine = Engine.create();
  const queue = [];

  const spawnBox = () => {
    const box = Bodies.rectangle(100, 100, 50, 50, {restitution: 0.5})
    World.add(engine.world, box);

    queue.push(box);
  }

  onMount(() => {
    const render = Render.create({
      canvas: document.getElementById("canvas") as HTMLCanvasElement,
      engine: engine
    });

    const ground = Bodies.rectangle(400, 610, 810, 70, {isStatic: true, restitution: 1});
    const box = Bodies.rectangle(400, 100, 50, 50, {restitution: 1});
    Composite.add(engine.world, [ground, box]);

    Render.run(render);

    const runner = Runner.create()

    Runner.run(runner, engine);

    let mouseConstraint = Matter.MouseConstraint.create(
      engine, 
      {
        mouse: Mouse.create(render.canvas),
        constraint: {
            stiffness: 1,
            render: {
                visible: false
            },
        }
      });
    World.add(engine.world, mouseConstraint);

    setInterval(() => spawnBox(), 4000)
    setInterval(() => {
      if (queue.length > 6) {
        Composite.remove(engine.world, queue.shift());
      }
    }, 1500)
  })
</script>
  
  <main>
    <h1>Queue</h1>
    <canvas id="canvas"></canvas>
  </main>
  
  <style>
    main {
      text-align: center;
      padding: 1em;
      max-width: 240px;
      margin: 0 auto;
    }
  
    canvas {
      height: auto;
      width: 80%;
    }
  
    @media (min-width: 640px) {
      main {
        max-width: none;
      }
    }
  </style>