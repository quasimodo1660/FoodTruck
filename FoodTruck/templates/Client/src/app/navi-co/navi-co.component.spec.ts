import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NaviCoComponent } from './navi-co.component';

describe('NaviCoComponent', () => {
  let component: NaviCoComponent;
  let fixture: ComponentFixture<NaviCoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NaviCoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NaviCoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
