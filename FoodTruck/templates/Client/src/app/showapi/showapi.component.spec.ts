import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowapiComponent } from './showapi.component';

describe('ShowapiComponent', () => {
  let component: ShowapiComponent;
  let fixture: ComponentFixture<ShowapiComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShowapiComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShowapiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
