import { Component } from '@angular/core';

@Component({
  selector: 'app-logo',
  imports: [],
  template: `
    <section>
      <form>
        <input type="text" placeholder="Filter by city"/>
        <button class="primary" type="button">Search</button>
      </form>
    </section>
  `,
  styleUrls: ['./logo.component.css'],
})
export class LogoComponent {

}
