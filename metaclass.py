Foo = type('Foo', (), {'bar': True})


def echo_bar(self):
    print(self.bar)


FooChild = type('FooCHild', (Foo,), {'echo_bar': echo_bar})

print(hasattr(FooChild, 'echo_bar'))


f = FooChild()
f.echo_bar()

print(type(f))
