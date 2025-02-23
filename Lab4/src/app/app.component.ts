import {Component} from '@angular/core';
import {LogoComponent} from './logo/logo.component';
import {NgOptimizedImage} from "@angular/common";

@Component({
  selector: 'app-root',
  imports: [
    NgOptimizedImage,
    LogoComponent
  ],
  template: `
    <main>
      <header class="brand-name">
        <img class="brand-logo" src="assets/logo.svg" alt="logo"/>
      </header>
      <section class="content">
        <app-logo></app-logo>
      </section>
    </main>`,
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  title = 'products';
}
